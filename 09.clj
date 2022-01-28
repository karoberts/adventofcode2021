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

(defn find-adj-coord [grid x y]
  (remove
    #(nil? (grid %1))
    (map
      (fn[adj]
        [(+ x (adj 0)) (+ y (adj 1))])
      adj-map)))

(defn find-lowest-basins [grid]
  (filter
    (fn[gk]
      (let [coord (gk 0)
            v (gk 1)
            x (coord 0) y (coord 1)]
        (every? boolean
          (map
            #(> %1 v)
            (map grid (find-adj-coord grid x y))))))
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

(defn calc-basin-size
  ([grid coord] (calc-basin-size grid coord (atom #{})))
  ([grid coord visited]
    (if (or (contains? @visited coord) (= (grid coord) 9))
      0
      (let [x (coord 0)
            y (coord 1)
            adj (find-adj-coord grid x y)]
        (swap! visited conj coord)
        (inc
          (reduce +
            (map
              #(calc-basin-size grid %1 visited)
              adj)))))))

(def basin-sizes
  (->>
    (map
      #(calc-basin-size grid %1)
      (map
        #(%1 0)
        lowest-pts))
    sort
    reverse
    (take 3)
    (reduce *)))
(println "part2" basin-sizes)
