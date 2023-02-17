#ask 6 questions to the user about wha car they want to buy
# - one multiple choice
# - one yes or no
# - one short response
#
#summary of user choices

# Intro header for form
print("===============================")
print("Welcome to Automotive Enthusiast Werks!")
print("No automatics allowed here")
print("===============================")
print("")

#first question (multiple choice)
print("1) What drivetrain configuration would you like? ")
print("a. Front-Wheel Drive (FWD)")
print("b. Rear-Wheel Drive (RWD)")
print("c. All-Wheel Drive (AWD")
print("d. 4-wheel drive (4WD")
userDriveTrain = input("Please enter 'a' - 'd': ")
print("")

#second question ('yes' or 'no')
print("2) Would you like an automatic transmission? ")
userTransmission = input("Please enter 'yes' or 'no':")
print("")

#This part is just for fun and for me to refresh on while loops
#while I was able to get the loop to trigger on yes, I was not able to break it correctly with 
#the user inputting 'no'; instead any response other then 'yes' breaks the loop
while userTransmission == 'yes':
  print("We don't allow that here...")
  userTransmission = input("Please enter 'yes' or 'no':")
  print("")
  if userTransmission == 'no':
    break
  
    
print("")


#third question (short response)
userAirFresh = input("3) What flavor would you like for your complimentary air freshener? ")
print("")

#4th question ('yes' or 'no')
print("4) Would you like your tires to be upgraded to racing slicks?")
userRaceSlick = input("Please enter 'yes' or 'no': ")
print("")

#5th question (multiple choice)
print("5) What type of aspiration would you like for your engine?")
print("a. Naturally Aspirated")
print("b. Turbocharged")
print("c. Supercharged")
userEngine = input("Please enter 'a' - 'c': ")
print("")

#sixth question ('yes' or 'no')
print("6) Would you like the interior stripped with the exception of the driver seat?")
userInteriorStrip = input("Please enter 'yes' or 'no': ")
print("")

#output summary of user choices
print("===============================")
print("-----Configuration Summary-----")
print(f"Drivetrain Configuration: {userDriveTrain}")
print(f"Downgrade to Autotragic Transmission: {userTransmission}")
print(f"Air Freshener Flavor: {userAirFresh}")
print(f"Upgrade to Racing Slicks: {userRaceSlick}")
print(f"Engine Aspiration: {userEngine}")
print(f"Remove interior: {userInteriorStrip}")

