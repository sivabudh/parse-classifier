from pyparsing import *

classifier = """
  User Defined Classifier Information:
   Classifier: vlan181
    Operator: AND
    Rule(s) : if-match vlan-id 181


   Classifier: 12345
    Operator: AND
    Rule(s) : if-match vlan-id 182


   Classifier: 123456
    Operator: AND
    Rule(s) : if-match vlan-id 1616


   Classifier: vlan181_tcp
    Operator: AND
    Rule(s) : if-match vlan-id 181

              if-match acl 3010


   Classifier: vlan181_udp
    Operator: AND
    Rule(s) : if-match vlan-id 181

              if-match acl 3011
"""

policy = """
  User Defined Traffic Policy Information:
  Policy: EPL
   Classifier: 123456
    Operator: AND
     Behavior: 123456
        Committed Access Rate:
        CIR 10500 (Kbps), CBS 775000 (Byte)
        Conform Action : pass
        Exceed  Action : discard

  Policy: Test_agg_40M
   Classifier: vlan181_tcp
    Operator: AND
     Behavior: agg_40M_tcp
        Committed Access Rate:
        CIR 58000 (Kbps), CBS 4495000 (Byte)
        Conform Action : pass
        Exceed  Action : discard
        car aggregation
   Classifier: vlan181_udp
    Operator: AND
     Behavior: agg_40M_udp
        Committed Access Rate:
        CIR 42000 (Kbps), CBS 3100000 (Byte)
        Conform Action : pass
        Exceed  Action : discard
        car aggregation

Total policy number is 2
"""

print(classifier)
print(policy)

word = Word(alphas + "'.")
salutation = OneOrMore(word)
comma = Literal(",")
greetee = OneOrMore(word)
endpunc = oneOf("! ?")
greeting = salutation + comma + greetee + endpunc

results = greeting.parseString("Yo, what's up?")
print(results)
