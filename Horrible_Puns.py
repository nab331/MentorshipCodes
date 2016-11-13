def print_points():
	print "\n\t\t\tLevel  : ", "1" , "2" , "3"
	print "\t\t\tPoints : ", pun1_points , pun2_points , pun3_points

def display_score(n_p1,n_p2,n_p3):
	print "\n\n_______________________________________________________________________________________________________"

	print "You Scored ", pun1_points," out of ",n_p1," in your first test\nYour Percentage is ", round((float(pun1_points) * 100 /n_p1),2)
	if (float(pun1_points)/n_p1) < 0.4:
		print "You failed0\n"
	else:
		print "You passed\n"

	print "You Scored ", pun2_points," out of ",n_p2," in your first test\nYour Percentage is ", round((float(pun2_points) * 100 /n_p2),2)
	if (float(pun1_points)/n_p2) < 0.4:
		print "You failed\n"
	else:
		print "You passed\n"

	print "You Scored ", pun3_points," out of ",n_p3," in your first test\nYour Percentage is ", round((float(pun3_points) * 100 /n_p3),2)
	if (float(pun1_points)/n_p3	) < 0.4:
		print "You failed\n"
	else:
		print "You passed\n"


	print "_______________________________________________________________________________________________________"




print "Welcome to Horrible puns, Lets see how strong your pun game is..."

pun1 = {"What's the worst thing about throwing a party in space? You Have to _ _ _ _ _ _":"Planet",
		"It was an emotional wedding. Even the cake was in _ _ _ _ _":"Tiers",
		"What does a house wear? A _ _ _ _ _":"Dress",		
		"I asked a Frenchman if he played video games. He said _ _ _": "Wii"


}


pun2 = {"Why couldn't the bicycle stand up on its own? It was _ _ _  _ _ _ _ _":"Two Tired",
		"How did I escape Iraq? _ _ _ _" : "Iran",
		"I'm glad I know sign language, it's pretty _ _ _ _ _" : "Handy",




}
pun3 = {"The furniture store keeps calling me to come back. But all i wanted was a  _ _ _  _ _ _ _ _  _ _ _ _ _" :"One Night Stand",
		"Did you hear about the guy who jumped off a bridge in Paris? He was in _ _ _ _ _": "Seine",
		"Did you hear about the guy who got hit in the head with a can of soda? He was lucky it was a _ _ _ _  _ _ _ _ _ ":"Soft Drink",
}

n_p1 = len(pun1)
n_p2 = len(pun2)
n_p3 = len(pun3)

global pun1_points
global pun2_points
global pun3_points

pun1_points , pun2_points , pun3_points = 0 , 0 , 0


print "\n*******************************LEVEL 1 (",n_p1 , "Questions) ******************************"

for key,value in pun1.items():
	print
	print
	print_points()
	print key
	answer = raw_input("Enter your Answer : ")
	if answer.lower() == value.lower():
		print "Correct"
		pun1_points+= 1

	else:
		print "Wrong Answer, the correct answer is : ",value 		


print "\n*******************************LEVEL 2 (",n_p2 , "Questions) ******************************"

for key,value in pun2.items():
	print
	print
	print_points()
	print key
	answer = raw_input("Enter your Answer : ")
	if answer.lower() == value.lower():
		print "Correct"
		pun2_points+= 1

	else:
		print "Wrong Answer, the correct answer is : ",value 	



print "\n*******************************LEVEL 3 (",n_p3 , "Questions) ******************************"

for key,value in pun3.items():
	print
	print
	print_points()
	print key
	answer = raw_input("Enter your Answer : ")
	if answer.lower() == value.lower():
		print "Correct"
		pun3_points+= 1

	else:
		print "Wrong Answer, the correct answer is : ",value 	



display_score(n_p1,n_p2,n_p3)