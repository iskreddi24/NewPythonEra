name=input('Enter the name: ')
age=int(input('Enter the age: '))
have_voterid=True
have_valid_proof=True
def votepunch(name,age,have_voterid,have_valid_proof):
    if age<=18:
        return 'Not eligible for vote'
    if not have_voterid:
        return 'Without voter id also you are not eligible'
    if not have_valid_proof:
        return 'are you a terrorist'
    if age>=18 and have_voterid and have_valid_proof:
        return 'Eligible to vote ',name
result=votepunch(name,age,have_voterid,have_valid_proof)
print(result)