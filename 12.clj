(def lines (clojure.string/split-lines (slurp "12.txt")))

(defn build-tree-from-edges [edges tree]
  (if (empty? edges)
    tree
    (let [e (first edges)
          e1 (e 0)
          e2 (e 1)]
      (recur
        (rest edges)
        (as-> tree $
          (assoc $ e1 (conj (tree e1 #{}) e2))
          (assoc $ e2 (conj (tree e2 #{}) e1)))))))

(defn build-tree [lines]
  (let [edges 
        (->> lines
          (map #(clojure.string/split %1 #"\-"))
          (map (fn[x] [[(first x) (second x)] [(second x) (first x)]]))
          (apply concat))]
    (build-tree-from-edges edges {})))

(defn is-lowercase [s]
  (= s (clojure.string/lower-case s)))

(defn count-paths [tree node visited]
  (reduce +
    (for [dest (tree node)]
      (if (contains? visited dest)
        0
        (if (= dest "end")
          1
          (count-paths
            tree
            dest
            (if (is-lowercase dest)
              (conj visited dest)
              visited)))))))

(def tree (build-tree lines))
;(println tree)
(println "part1" (count-paths tree "start" #{"start"}))

