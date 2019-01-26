import os, sys

#the path of current working deriction will be assigned to path and files in the direction will assigne to dirs
path = os.getcwd()
dirs = os.listdir(path)

#this will filter the file inside folder and create all list that contain just full path of files with extension url
path_filtered= []
for i in dirs:
   if i.split(".")[-1] == 'url':
      path_filtered.append(path + "\\"[0] + i )

#this will print the number of file with extension url inside the folder 
print (str(len(path_filtered))+" file with File extension \'url\' found")
print ("if you want to print all files write yes, if just a part of them write no")

#this will open all url in the folder
def all_of():
   for li in path_filtered:
      os.startfile(li ,'open')

#this will the part that you chose
def part_of(start, end):
   try:
      a= start
      b=end
      for li in path_filtered[a:b]:
         os.startfile(li ,'open')
   except:
      print ("what you wrote is not a number")
      print("try again")
      print ("write a start number")
      c = int(input())
      print ("write an end number ")
      d = int(input())
      part_of(c, d)

#this to choose which function to use
def which_way(way):
   num = way
   if num == "yes":
      return all_of()
   elif num == "no" :
      print ("write a start number")
      a = int(input())
      print ("write an end number ")
      b = int(input())
      return part_of(a,b )     
   else:
      print("what you wrote is not a number or wrong number " +'\n'+ 'try again')
      in_put = int(input())
      return which_way(in_put)

which_way(input())