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

(defn get-paths2 [tree node visited path uniq smallcave smallcaveCt]
  (for [dest (tree node)]
    (if (and (contains? visited dest) (or (not= dest smallcave) (= smallcaveCt 2)))
      uniq
      (if (= dest "end")
        (conj uniq (clojure.string/join "|" path))
        (get-paths2
          tree
          dest
          (if (is-lowercase dest)
            (conj visited dest)
            visited)
          (conj path dest)
          uniq
          smallcave
          (+ smallcaveCt (if (= dest smallcave) 1 0)))))))

(defn count-unique-paths2 [tree]
  (let [paths
          (for [cave (filter #(and (is-lowercase %) (not= "end" %) (not= "start" %)) (keys tree))]
            (get-paths2 tree "start" #{"start"} [] [] cave 0))]
    (->> paths flatten set count)))

(println "part2" (count-unique-paths2 tree))