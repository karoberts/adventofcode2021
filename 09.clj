(load-file "grids.clj")
(load-file "utils.clj")

(defn find-adj-coord [grid x y]
  (remove
    #(nil? (grid %1))
    (map
      (fn[adj]
        [(+ x (adj 0)) (+ y (adj 1))])
      grids/adjacent-list)))

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

(def lines (utils/read-lines "9.txt"))

(def grid (grids/parse-int-grid lines))

(def lowest-pts (find-lowest-basins (grid :grid)))
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
      #(calc-basin-size (grid :grid) %1)
      (map
        #(%1 0)
        lowest-pts))
    sort
    reverse
    (take 3)
    (reduce *)))
(println "part2" basin-sizes)
