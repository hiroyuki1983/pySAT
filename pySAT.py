# -*- encoding:utf-8 -*-


def delete_literal(clause, literal):
	temp = clause
	del temp[temp.index(literal)]
	return temp


def contract_clause(CNF, literal):
	contracted_CNF = []
	dual_literal = 0 - literal
	for clause in CNF:
		if literal in clause:
			continue # do nothing
		else:
			contracted_CNF.append(clause) # do nothing and add clause to list for return
	return contracted_CNF



def convert2cnf_list(input):
	import re
	cnf_pattern1 = re.compile('\(-?[0-9]+(\|-?[0-9]+)*\)(\&\(-?[0-9]+(\|-?[0-9]+)*\))*')
	cnf_pattern2 = re.compile('^\(-?[0-9]+.*\)$')
	cnf_pattern3 = re.compile('^\(.*-?[0-9]+\)$')

	if not (cnf_pattern1.match(input) and cnf_pattern2.match(input) and cnf_pattern3.match(input)):
		print "Input Error! Your input '" + input + "' is not expected form."
		return 0

	input = input.replace('(', '')
	input = input.replace(')', '')
	outer_list = input.split('&')
	outer_answer_list = []
	for inner_list in outer_list:
		most_inner_list = inner_list.split('|')
		inner_answer_list = []
		for x in most_inner_list:
			inner_answer_list.append(int(x))
		outer_answer_list.append(inner_answer_list)

	return satSolver(outer_answer_list)


def satSolver(CNF):
	ans = []
	list = []
	list.append(False)
	ans = satSolve(CNF, list)
	if ans[0] == True:
		return ans[1:]
	else:
		return ans[0]


def satSolve(CNF, list=[]):
	if len(CNF) == 0:
		list[0] = True
		return list

	top_literal = CNF[0][0]
	dual_literal = 0 - top_literal

	if top_literal in list:
		return list

	if dual_literal in list:
		return list

	list.append(top_literal)
	list = satSolve(contract_clause(CNF, top_literal), list)

	if list[0] == True:
		return list

	list.append(dual_literal)
	list = satSolve(contract_clause(CNF, dual_literal), list)

	return list



input = raw_input('Please input CNF >> ')
print convert2cnf_list(input)



