(ns utils
  "utilities for aoc")

(def parseInt
  "handy variable for using a parseInt func as a parameter"
  #(Integer/parseInt %))

(def parseLong
  "handy variable for using a parseLong func as a parameter"
  #(Long/parseLong %))

(defn read-lines
  "read a text file and return a vector of lines"
  [filename] (clojure.string/split-lines (slurp filename)))

(defn read-lines-map
  "read a text file and return a vector of the result of a function on each line"
  [filename func] 
    (mapv
      func
      (clojure.string/split-lines (slurp filename))))

(defn read-lines-map-split
  "read a text file and return a vector of the result of a function on each character in each line"
  [filename func] 
    (mapv
      (fn[line] 
        (map 
          func
          (clojure.string/split line #"")))
      (clojure.string/split-lines (slurp filename))))