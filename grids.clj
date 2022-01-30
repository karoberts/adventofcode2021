(load-file "utils.clj")

(ns grids
  "Grid helpers")

(def adjacent-list
  "an adjacent list for up/down/left/right.  Add to coord"
  '( [-1 0] [0 -1] [1 0] [0 1] ))

(def adjacent-list-all
  "an adjacent list for all 8 adjacent cells.  Add to coord"
  '( [-1 -1] [0 -1] [1 -1] [-1 0] [1 0] [-1 1] [0 1] [1 1] ))

(defn- parse-line-impl [line y xdim f]
  (into {}
    (map 
      (fn[v x] {[x y] (f v)})
      (clojure.string/split line #"")
      (range xdim))))

(defn- parse-grid-impl [lines xdim ydim y grid func]
  (into {}
    (for
      [i (map
          (fn[idx val] [idx val])
          (range ydim)
          lines)]
        (parse-line-impl (i 1) (i 0) xdim func))))

(defn parse-grid "parse a grid from lines into {:grid, :xdim, :ydim}" 
  ([lines] (parse-grid lines identity))
  ([lines func]
    (let [ydim (count lines)
          xdim (count (first lines))]
      {:grid (parse-grid-impl lines xdim ydim 0 {} func), :xdim xdim, :ydim ydim})))

(defn parse-int-grid "parse a grid containing ints 0-9 from lines into {:grid, :xdim, :ydim}" 
  [lines] (parse-grid lines utils/parseInt))

(defn print-grid "print a grid parsed by 'parse-grid'" [grid]
  (let [g (grid :grid)]
    (doseq [y (range 0 (grid :ydim))]
      (doseq [x (range 0 (grid :xdim))]
        (print (g [x y])))
      (newline))))