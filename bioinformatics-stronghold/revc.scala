// Problem ID: REVC
// Complementing a strand of DNA

import scala.io.Source

def reverseComplement(s: String): String = {
    var pairs = Map('A' -> 'T', 'T' -> 'A', 'C' -> 'G', 'G' -> 'C')
    s.trim.reverse.map(pairs(_))
}

val s = "AAAACCCGGT"
assert(reverseComplement(s) == "ACCGGGTTTT")

var file = Source.fromFile("data/rosalind_revc.txt").mkString
println(reverseComplement(file))