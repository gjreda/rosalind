// Problem ID: RNA
// Transcribing DNA to RNA

import scala.io.Source

def transcribeRNAtoDNA(s: String): String = {
    s.trim.replace('T', 'U')
}

val s = "GATGGAACTTGACTACGTAAATT"
assert(transcribeRNAtoDNA(s) == "GAUGGAACUUGACUACGUAAAUU")

var line = Source.fromFile("data/rosalind_rna.txt").mkString
println(transcribeRNAtoDNA(line))