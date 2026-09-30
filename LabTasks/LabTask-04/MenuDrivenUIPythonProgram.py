import tkinter as tk
from tkinter import ttk, messagebox
import heapq
import random
from collections import deque


# =====================================================================
#  GRAPH DATA STRUCTURE
# =====================================================================
class Graph:
    """Stores nodes and weighted directed/undirected edges."""

    def __init__(self):
        # adjacency list: {node: [(neighbor, cost), ...]}
        self.adj = {}

    def add_node(self, node):
        self.adj.setdefault(node, [])

    def add_edge(self, u, v, cost, bidirectional=True):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, cost))
        if bidirectional:
            self.adj[v].append((u, cost))

    def neighbors(self, node):
        return self.adj.get(node, [])


# =====================================================================
#  ALGORITHM 1 : RANDOM SEARCH   (Lecture slide 33)
# =====================================================================
def random_search(graph, start, goal, max_steps=1000):
    """
    Randomly pick one child at each step until goal is reached.
    Returns (path, cost, success).
    """
    current = start
    path = [current]
    total_cost = 0

    for _ in range(max_steps):
        if current == goal:
            return path, total_cost, True

        nbrs = graph.neighbors(current)
        if not nbrs:
            return path, total_cost, False   # dead end

        # pick a random neighbour
        nxt, cost = random.choice(nbrs)
        path.append(nxt)
        total_cost += cost
        current = nxt

    return path, total_cost, False   # exceeded step budget


# =====================================================================
#  ALGORITHM 2 : OPEN LIST + CLOSED LIST SEARCH  (Lecture slides 37–39)
# =====================================================================
def open_closed_search(graph, start, goal, use_queue=True):
    """
    Generic open-list / closed-list search.
      use_queue=True  -> BFS  (pop from front  -> FIFO)
      use_queue=False -> DFS  (pop from back   -> LIFO)

    Returns (path, cost, success).
    """
    open_list = [start]                  # fringe
    closed_list = set()                  # already expanded
    parent = {start: None}               # for path reconstruction
    cost_so_far = {start: 0}

    while open_list:
        # pop from front (BFS) or back (DFS)
        if use_queue:
            current = open_list.pop(0)
        else:
            current = open_list.pop()

        if current == goal:
            # reconstruct path
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, cost_so_far[current], True

        if current in closed_list:
            continue
        closed_list.add(current)

        for nbr, cost in graph.neighbors(current):
            if nbr not in closed_list:
                if nbr not in parent:           # first time discovered
                    parent[nbr] = current
                    cost_so_far[nbr] = cost_so_far[current] + cost
                    open_list.append(nbr)
                elif cost_so_far[current] + cost < cost_so_far.get(nbr, float('inf')):
                    # found a cheaper way to reach nbr
                    parent[nbr] = current
                    cost_so_far[nbr] = cost_so_far[current] + cost
                    if nbr not in open_list:
                        open_list.append(nbr)

    return [], 0, False     # failure


# =====================================================================
#  ALGORITHM 3 : UNIFORM-COST SEARCH (DIJKSTRA)   (Lecture slides 41–42)
# =====================================================================
def dijkstra(graph, start, goal):
    """
    Uniform-cost search using a priority queue (min-heap).
    Always returns the minimum-cost path.
    """
    open_list = [(0, start)]          # (accumulated cost, node)
    closed_list = set()
    parent = {start: None}
    cost_so_far = {start: 0}

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, current_cost, True

        if current in closed_list:
            continue
        closed_list.add(current)

        for nbr, step_cost in graph.neighbors(current):
            new_cost = current_cost + step_cost
            if nbr not in closed_list and new_cost < cost_so_far.get(nbr, float('inf')):
                cost_so_far[nbr] = new_cost
                parent[nbr] = current
                heapq.heappush(open_list, (new_cost, nbr))

    return [], 0, False


# =====================================================================
#  TKINTER GUI
# =====================================================================
class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Search Algorithms — UOK Assignment")
        self.geometry("780x620")
        self.configure(bg="#1e1e2e")

        self.graph = Graph()
        self.start_node = None
        self.goal_node = None

        self._build_ui()

    # ---------- UI CONSTRUCTION ----------
    def _build_ui(self):
        # Title
        tk.Label(self, text="🔍  AI Search Algorithm Playground",
                 font=("Segoe UI", 18, "bold"),
                 fg="#89b4fa", bg="#1e1e2e").pack(pady=10)

        # ---- Frame 1: Graph input ----
        input_frame = tk.LabelFrame(self, text=" 1️⃣  Build Your Graph ",
                                    font=("Segoe UI", 11, "bold"),
                                    fg="#cdd6f4", bg="#313244",
                                    padx=10, pady=10)
        input_frame.pack(fill="x", padx=15, pady=6)

        # Start node
        tk.Label(input_frame, text="Start Node:", fg="#cdd6f4",
                 bg="#313244").grid(row=0, column=0, sticky="w", pady=2)
        self.start_entry = tk.Entry(input_frame, width=10)
        self.start_entry.grid(row=0, column=1, padx=5)

        # Goal node
        tk.Label(input_frame, text="Goal Node:", fg="#cdd6f4",
                 bg="#313244").grid(row=0, column=2, sticky="w", padx=(15, 0))
        self.goal_entry = tk.Entry(input_frame, width=10)
        self.goal_entry.grid(row=0, column=3, padx=5)

        # Edge input
        tk.Label(input_frame, text="Edge (e.g.  A B 5):", fg="#cdd6f4",
                 bg="#313244").grid(row=1, column=0, columnspan=2,
                                    sticky="w", pady=(8, 2))
        self.edge_entry = tk.Entry(input_frame, width=20)
        self.edge_entry.grid(row=1, column=2, columnspan=2, sticky="w")

        # Add-edge button
        tk.Button(input_frame, text="➕ Add Edge", command=self.add_edge,
                  bg="#a6e3a1", fg="#1e1e2e", font=("Segoe UI", 9, "bold"),
                  relief="flat", padx=8).grid(row=1, column=4, padx=10)

        # Show-graph button
        tk.Button(input_frame, text="📋 Show Graph", command=self.show_graph,
                  bg="#89dceb", fg="#1e1e2e", font=("Segoe UI", 9, "bold"),
                  relief="flat", padx=8).grid(row=0, column=4, padx=10)

        # ---- Frame 2: Algorithm selection ----
        algo_frame = tk.LabelFrame(self, text=" 2️⃣  Choose Algorithm ",
                                   font=("Segoe UI", 11, "bold"),
                                   fg="#cdd6f4", bg="#313244",
                                   padx=10, pady=10)
        algo_frame.pack(fill="x", padx=15, pady=6)

        self.algo_var = tk.StringVar(value="Dijkstra")
        options = [
            ("Random Search", "random"),
            ("Open/Closed List Search (BFS)", "bfs"),
            ("Open/Closed List Search (DFS)", "dfs"),
            ("Dijkstra / Uniform-Cost Search", "dijkstra"),
        ]
        for text, val in options:
            tk.Radiobutton(algo_frame, text=text, variable=self.algo_var,
                           value=val, fg="#cdd6f4", bg="#313244",
                           selectcolor="#45475a",
                           activebackground="#313244",
                           font=("Segoe UI", 10)
                           ).pack(anchor="w")

        # ---- Run button ----
        tk.Button(self, text="▶  RUN SEARCH", command=self.run_search,
                  bg="#f9e2af", fg="#1e1e2e",
                  font=("Segoe UI", 13, "bold"),
                  relief="flat", padx=20, pady=6).pack(pady=12)

        # ---- Output ----
        out_frame = tk.LabelFrame(self, text=" 3️⃣  Result ",
                                  font=("Segoe UI", 11, "bold"),
                                  fg="#cdd6f4", bg="#313244",
                                  padx=10, pady=10)
        out_frame.pack(fill="both", expand=True, padx=15, pady=6)

        self.output = tk.Text(out_frame, height=10, bg="#181825",
                              fg="#a6e3a1", font=("Consolas", 11),
                              wrap="word", relief="flat")
        self.output.pack(fill="both", expand=True)

    # ---------- EVENT HANDLERS ----------
    def add_edge(self):
        raw = self.edge_entry.get().strip()
        parts = raw.split()
        if len(parts) != 3:
            messagebox.showerror("Input Error",
                                 "Format: <node1> <node2> <cost>\n"
                                 "Example: A B 5")
            return
        u, v, cost_str = parts
        try:
            cost = float(cost_str)
        except ValueError:
            messagebox.showerror("Input Error", "Cost must be a number.")
            return
        self.graph.add_edge(u, v, cost)
        self.edge_entry.delete(0, tk.END)
        self.log(f"✔ Added edge: {u} <--> {v}  (cost={cost})")

    def show_graph(self):
        self.log("\n📌 Current Graph:")
        if not self.graph.adj:
            self.log("   (empty — no edges added yet)")
            return
        for node, nbrs in self.graph.adj.items():
            if nbrs:
                nbr_str = ", ".join(f"{n}({c})" for n, c in nbrs)
                self.log(f"   {node}  →  {nbr_str}")
        self.log("")

    def run_search(self):
        # get start / goal
        start = self.start_entry.get().strip()
        goal = self.goal_entry.get().strip()

        if not start or not goal:
            messagebox.showerror("Input Error", "Please enter Start and Goal nodes.")
            return
        if start not in self.graph.adj or goal not in self.graph.adj:
            messagebox.showerror("Input Error",
                                 f"Unknown node(s). Known nodes: "
                                 f"{list(self.graph.adj.keys())}")
            return

        algo = self.algo_var.get()
        self.log("\n" + "=" * 50)

        if algo == "random":
            self.log("🎲 Running RANDOM SEARCH ...")
            path, cost, ok = random_search(self.graph, start, goal)

        elif algo == "bfs":
            self.log("📚 Running OPEN/CLOSED LIST SEARCH (BFS) ...")
            path, cost, ok = open_closed_search(self.graph, start, goal,
                                                use_queue=True)

        elif algo == "dfs":
            self.log("📚 Running OPEN/CLOSED LIST SEARCH (DFS) ...")
            path, cost, ok = open_closed_search(self.graph, start, goal,
                                                use_queue=False)

        else:  # dijkstra
            self.log("⚡ Running DIJKSTRA / UNIFORM-COST SEARCH ...")
            path, cost, ok = dijkstra(self.graph, start, goal)

        if ok:
            self.log(f"✅ SUCCESS!")
            self.log(f"   Path : {' → '.join(path)}")
            self.log(f"   Total cost : {cost}")
        else:
            self.log("❌ FAILURE — no path found to the goal "
                     "(or step limit reached).")
            if path:
                self.log(f"   Explored: {' → '.join(path)}")
        self.log("=" * 50 + "\n")

    # ---------- UTILITY ----------
    def log(self, msg):
        self.output.insert(tk.END, msg + "\n")
        self.output.see(tk.END)


# =====================================================================
#  MAIN
# =====================================================================
if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()