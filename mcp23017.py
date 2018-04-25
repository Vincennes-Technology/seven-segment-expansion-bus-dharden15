
         usage()
         sys.exit()
      elif opt in ("-b", "--bank"):
         bank = arg
      elif opt in ("-o", "--output"):
         output = int(arg)
      elif opt in ("-s", "--state"):
         state = arg

# Set the correct register for the banks
   if bank == "a" :
    register = 0x12
   elif bank == "b" :
    register = 0x13
   else:
    print "Error! Bank must be a or b"
    sys.exit()

# Read current values from the IO Expander
   value =  bus.read_byte_data(address,register)

# Shift the bits for the register value, checking if they are already set first
   if state == "high":
    if (value >> output) & 1 :
     print "Output GP"+bank.upper()+str(output), "is already high."
     sys.exit()
    else:
      value += (1 << output)
   elif state == "low":
    if (value >> output) & 1 :
     value -= (1 << output)
    else:
     print "Output GP"+bank.upper()+str(output), "is already low."
     sys.exit()
   elif state == "read":
    if (value >> output) & 1 :
     print "high"
    else:
     print "low"
    sys.exit()
   else:
    print "Error! state must be high or low"
    sys.exit()

# Now write to the IO expander
   bus.write_byte_data(address,register,value)

# Tell them what we did
   print "Output GP"+bank.upper()+str(output), "changed to", state

if __name__ == "__main__":
   main()