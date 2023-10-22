from insert import qa_chain, process_llm_response

# full example
query = "When does line 101 close?"
llm_response = qa_chain(query)
process_llm_response(llm_response)
