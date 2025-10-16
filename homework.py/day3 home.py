is_logged_in = True

is_subscribed = False

user_credits = 100
max_credits  = 200
min_credits  = 50

credits_valid  = (user_credits >= min_credits) and (user_credits <= max_credits) and (user_credits != min_credits)

bonus_eligible = is_subscribed or (user_credits > min_credits)

user_credits  = 100
user_credits += 50
user_credits -= 20
user_credits *= 2
user_credits %= 150

power_result = user_credits**2

full_access  = is_logged_in and is_subscribed

is_true_login = is_logged_in is True

access_result = is_logged_in or is_subscribed and False
print("is logged in:", is_logged_in)
print("is subscribed:", is_subscribed)
print("credits valid:", credits_valid)
print("bonus eligibility:", bonus_eligible)
print("user credits:", user_credits)
print("power result:", power_result)
print("full access", full_access)
print("true login", is_true_login)
print("access result", access_result)