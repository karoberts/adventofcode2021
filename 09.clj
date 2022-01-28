(defn parse-line [line y dim]
  (into {}
    (map 
      (fn[v x] {[x y] (Integer/parseInt v)})
      (clojure.string/split line #"")
      (range 0 dim))))

(defn parse-grid [lines xdim ydim y grid]
  (if (= y ydim)
    grid
    (parse-grid
      (rest lines)
      xdim
      ydim
      (inc y)
      (merge
        grid
        (parse-line (first lines) y xdim)))))

(defn print-grid [grid xdim ydim]
  (doseq [y (range 0 ydim)]
    (doseq [x (range 0 xdim)]
      (print (grid [x y])))
    (newline)))

(def adj-map [ [-1 0] [0 -1] [1 0] [0 1] ])

(defn find-lowest-basins [grid]
  (filter
    (fn[gk]
      (let [coord (gk 0)
            v (gk 1)
            x (coord 0) y (coord 1)]
        (every? boolean
          (map
            #(> %1 v)
            (remove
              nil?
              (map
                (fn[adj]
                  (grid [(+ x (adj 0)) (+ y (adj 1))]))
                adj-map))))))
    grid))

(def lines (clojure.string/split-lines (slurp "9.txt")))
(def ydim (count lines))
(def xdim (count (first lines)))

(def grid (parse-grid lines xdim ydim 0 {}))

(def lowest-pts (find-lowest-basins grid))
(def part1-ans
  (reduce +
    (map
      #(inc (%1 1))
      lowest-pts)))
(println "part1" part1-ans)

