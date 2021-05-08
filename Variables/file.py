import specialVar

print("File __name__  = %s" %__name__)

if __name__ == "__main__":
	print("File is being run directly")
else:
	print("File2 is being imported!")