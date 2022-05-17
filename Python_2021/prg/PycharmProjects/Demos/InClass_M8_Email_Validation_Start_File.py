# this function will test for a valid email address using standards and conventions
# an email address looks like: local-part@domain
# DOMAIN:
#   the domain must have at least two parts separated by a period, but may have more
#   the top-level domain (last part) must be alphabetic only
#   the other domain parts may contain letters, digits, or a hyphen
#   each part must start with a letter and end with a letter or digit
# LOCAL-PART:
#   although more characters are allowed by the standard, this program follows common usage conventions
#   multiple parts may be specified separated by a period (double period not allowed)
#   allowed characters for each part are: letters, digits, hyphens, and underscores
#   parts may not end with hyphen or underscore
def is_valid_email(email):
	# this function will test the domain part of the email address
	def is_domain_valid(full_domain):
		# first look at the domain, it must have at least two parts separated by periods
		domain_parts = full_domain.split(".")
		if len(domain_parts) < 2:
			return False
		# the top level domain (last item in list) must be alphabetic
		if not domain_parts[-1].isalpha():
			return False
		# for each of the remaining domain parts:
		#  They must start with a letter, end with a letter or digit, and have as interior characters
		#    only letters, digits, and hyphen.
		for part in domain_parts:
			# the length will be zero for a double period in the domain
			if len(part) == 0:
				return False
			# must begin with a letter
			elif not part[0].isalpha():
				return False
			# must not end with -
			elif part.endswith("-"):
				return False
			else:
				# make sure only letters, numbers, or hyphens included
				for char in part:
					if not char.isalnum() and not char == "-":
						return False
		# if none of the tests failed, the domain is valid
		return True

	# this function will test the local_part of the email address
	# this test is more restrictive than the standard, but conforms to common usage
	def is_local_part_valid(full_local_part):
		# first split the local_part on periods if there are any
		# period is not required but if there are any, cannot be two or more consecutive
		parts = full_local_part.split(".")
		# check the individual parts
		for one_part in parts:
			# test for consecutive periods in the full_local_part (an empty string in the list)
			if len(one_part) == 0:
				return False
			# must not end with - or _
			elif one_part.endswith(("-", '_')):
				return False
			else:
				# test for remaining characters being alphanumeric or underscore or hyphen
				for char in one_part:
					if not char.isalnum() and char not in "-_":
						return False
		# if none of the tests failed, the local_part is valid
		return True

	# split the email into two parts, the local_part and the domain
	# if the conversion to a tuple fails, there is no need to pursue additional testing
	try:
		local_part, domain = tuple(email.split("@"))
	except ValueError:
		return False
	# if splitting the email succeeds, test the two parts and return the result
	return is_domain_valid(domain) and is_local_part_valid(local_part)


# the main program just gets input from the user and validates it using is_valid_email()
def main():
	email = input("Enter your email address: ")
	if is_valid_email(email):
		print("Your email address is valid.")
	else:
		print("That is not a valid email.")


main()
