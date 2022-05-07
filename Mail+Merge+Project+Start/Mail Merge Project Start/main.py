names=[]

with open('C:/Users/Sarvjeet Bhardwaj/OneDrive/Documents/kaggle data/Projects/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt') as f_names:
    for name in  f_names.readlines():
        names.append(name.strip())

for invite_names in names:
    with open('C:/Users/Sarvjeet Bhardwaj/OneDrive/Documents/kaggle data/Projects/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/'+invite_names+'.txt', 'w') as f_output:
        f_output.write('Hello ' + invite_names)
        f_output.write('\n\n')
        f_output.write('You are invited to my birthday this Saturday.')
        f_output.write('\n\n')
        f_output.write('Hope you can make it.')
        f_output.write('\n\n')
        f_output.write('Angela')





