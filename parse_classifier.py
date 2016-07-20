import jtextfsm as textfsm

# Load the input file to a variable
input_file = open("parse_classifier.txt", encoding='utf-8')
raw_text_data = input_file.read()
input_file.close()

# Run the text through the FSM.
# The argument 'template' is a file handle and 'raw_text_data' is a
# string with the content from the show_inventory.txt file
template = open("parse_classifier.templ")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(raw_text_data)

# ...now all rows which were parsed by TextFSM
for row in fsm_results:
    print(row)
print("Write %d records" % len(fsm_results))
