// Problem ID: DNA
// Counting DNA nucleotides

import scala.io.Source

def printNucleotideCounts(s: String): String = {
    val counts = s.trim.groupBy(c => c).mapValues(_.length)
    s"${counts('A')} ${counts('C')} ${counts('G')} ${counts('T')}"
}

val s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
assert(printNucleotideCounts(s) == "20 12 17 21")

val line = Source.fromFile("data/rosalind_dna.txt").mkString
println(printNucleotideCounts(line))