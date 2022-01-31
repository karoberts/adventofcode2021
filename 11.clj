(load-file "utils.clj")
(load-file "grids.clj")

(def grid (grids/parse-int-grid (utils/read-lines "11.txt")))

(defn find-adj-coord [grid x y]
  (remove
    #(nil? (grid %1))
    (map
      (fn[adj]
        [(+ x (adj 0)) (+ y (adj 1))])
      grids/adjacent-list-all)))

(defn count-flashes [grid flashed]
  (let [will-flash (filter #(and (not (contains? flashed (%1 0))) (> (%1 1) 9)) grid)
        new-flashed (into #{} (map #(%1 0) will-flash))]
    (if (empty? new-flashed)
      [grid flashed]
      (count-flashes
        (reduce
          (fn[a c] 
            (if (contains? flashed c)
              a
              (assoc a c (inc (a c)))))
          grid
          (apply concat (for [f will-flash]
            (find-adj-coord grid ((f 0) 0) ((f 0) 1)))))
        (apply conj flashed new-flashed)))))

(defn run-step [grid]
  (let [inc-grid (reduce (fn [a v] (assoc a (v 0) (inc (v 1)))) {} grid)
        r (count-flashes inc-grid #{})
        next-grid (r 0)
        flashed (r 1)]
    [(into next-grid (for [f flashed] [f 0])) flashed]))

(def g (grid :grid))
(def ng
  (reduce 
    (fn[a v]
      (let [r (run-step (a 0))]
        [(r 0) (+ (a 1) (count (r 1)))]))
    [g 0]
    (range 100)))

;(grids/print-grid (merge grid {:grid (ng 0)}))
(println "part1" (ng 1))
