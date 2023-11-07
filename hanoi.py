def TowerOfHanoi(n , source, auxiliary, destination):
	if n==1:
		print ("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, destination, auxiliary)
	print ("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, source, destination)
		

n = 3
TowerOfHanoi(n,'A','B','C') 
