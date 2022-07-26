#Sorting the users into their respective groups, i.e their gender and what they're looking for

les = []
gays = []
bi_males = []
str_males = []
bi_females = []
str_females = []

def sort_users(profile_list):
    if len(profile_list)<=1:
        message = "Fail"
        pass_seeker_and_candidate(message)
    else:
        for user in profile_list:
            if (user["gender"] == "Male") & (user["virtue"]["genderPreference"] == "Female"):
                #print("straight male: "+user["profileName"])
                str_males.append(user)
            elif (user["gender"] == "Female") & (user["virtue"]["genderPreference"] == "Male"):
                #print("straight female: " + user["profileName"])
                str_females.append(user)
            elif (user["gender"] == "Female") & (user["virtue"]["genderPreference"] == "Female"):
                #print("lesbian: " + user["profileName"])
                les.append(user)
            elif (user["gender"] == "Male") & (user["virtue"]["genderPreference"] == "Male"):
                #print("gay: " + user["profileName"])
                gays.append(user)
            elif (user["gender"] == "Female") & (user["virtue"]["genderPreference"] == "Both"):
                #print("bi female: " + user["profileName"])
                bi_females.append(user)
            else:
                #print("bi male: " + user["profileName"])
                bi_males.append(user)
        message = "Success"
        pass_seeker_and_candidate(message)
category_list = [str_males, les, gays, bi_males, str_females, bi_females]

########################################################################################################################
#Passes list1(seeker) and list2(concatenated list of candidates from various categories) to the find partners function
def pass_seeker_and_candidate(message):
  if message == "Fail":
    print(message)
  else:
    nums = [
      {0: [4, 5]},
      {1: [1, 5]},
      {2: [2, 3]},
      {3: [4, 5]},
    ]
    for i in range(4):
      list1 = category_list[i]
      list2 = category_list[nums[i][i][0]] + category_list[nums[i][i][1]]
      find_partners_for(list1,list2)
      #print(list1,list2)

########################################################################################################################
#Couple compatibility functions. They each read in virtues between profiles and return a couple rating.

def ethnic_compatibility(pers1_ethnicity, pers2_ethnicity):
  if pers1_ethnicity == pers2_ethnicity:
    e_rating = 1
    return e_rating
  else:
    e_rating = 0.5
    return e_rating


def religious_compatibility(pers1_religion, pers2_religion):
  if pers1_religion == pers2_religion:
    r_rating = 2
    return r_rating
  elif (pers1_religion == "Agnostic" or "Atheist") and (pers2_religion != "Agnostic" or "Atheist"):
    r_rating = 0.5
    return r_rating
  else:
    r_rating = 1
    return r_rating

def political_compatibility(pers1_politics, pers2_politics):
  if pers1_politics == pers2_politics:
    p_rating = 1
    return p_rating
  else:
    p_rating = 0.5
    return p_rating

def smoke_compatibility(pers1_smoke, pers2_smoke):
  if pers1_smoke == pers2_smoke:
    s_rating = 1
    return s_rating
  else:
    s_rating = 0.5
    return s_rating

def drink_compatibility(pers1_drink, pers2_drink):
  if pers1_drink == pers2_drink:
    d_rating = 1
    return d_rating
  else:
    d_rating = 0.5
    return d_rating

def height_compatibility(pers1_height, pers2_height):
  if pers1_height == pers2_height:
    h_rating = 2
    return h_rating
  else:
    h_rating = 1
    return h_rating

########################################################################################################################
#THIS IS THE FUNCTION RESPONSIBLE FOR READING IN 2 LISTS(SEEKERS, CANDIDATES) AND RETURNS APPENDS A NEW LIST TO EACH USER
#PROFILE. ONE FOR RECOMMENDED MATCHES AND ONE FOR ALREADY RECOMMENDED. ONCE RECOMMENDED, THAT PARTICULAR USER WILL BE
#REMOVED FROM THE FORMER AND APPENDED TO THE LATTER.

def find_partners_for(list1, list2):
  # INTERESTS RATING
  matches = []
  for i in range(len(list1)):
    l1_interests = []
    seeker = list1[i]
    matches.append(seeker["profileName"])
    for s_interests in seeker["interests"]:
      l1_interests.append(s_interests["interestName"])
    #print(l1_interests)

    for j in range(len(list2)):
      tot_rating = 0
      common_interests = 0
      l2_interests = []
      candidate = list2[j]

      tot_rating += ethnic_compatibility(seeker["virtue"]["ethnicity"], candidate["virtue"]["ethnicity"])
      tot_rating += religious_compatibility(seeker["virtue"]["religion"], candidate["virtue"]["religion"])
      tot_rating += political_compatibility(seeker["virtue"]["politicalView"], candidate["virtue"]["politicalView"])
      tot_rating += smoke_compatibility(seeker["virtue"]["smoking"], candidate["virtue"]["smoking"])
      tot_rating += drink_compatibility(seeker["virtue"]["drinking"], candidate["virtue"]["drinking"])
      tot_rating += height_compatibility(seeker["virtue"]["height"], candidate["virtue"]["height"])

      for c_interests in candidate["interests"]:
        l2_interests.append(c_interests["interestName"])
      #print(l2_interests)

      for s_int in l1_interests:
        if s_int in l2_interests:
          common_interests += 1
      print(seeker["profileName"] ,candidate["profileName"] ,tot_rating+common_interests)

    # for j in range(len(list2)):
    #   l2_interests.append(list2[j]["interests"][j]["interestName"])


########################################################################################################################

#THE MAIN FUNCTION THAT CALLS ALL THE NECESSARY SUBORDINATE FUNCTIONS TO FACILITATE THE MATCHING PROCESS
def main():
  sort_users(Profiles)
  #print(category_list)

main()
########################################################################################################################
