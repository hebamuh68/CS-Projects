# OS simulation

It's a Python project to simulate the operating system.



## Classes & Functions

1. #### **Class CMD:** 

   - ***shell_commands()*** This use OS library to access shell commands through the IDE

     

2. #### **Class Virtual-disk:**

   - ***Instructor()*** 

     - create text file of 1 MB contains 1024 clusters/Blocks of size 1024 byte 

     - first cluster full of "0" =========> Super_Block

     - The next 4 cluster full of "*" ====> Meta_Data

     - The rest of 1 MB contain "#" ====> File_Data

       

   - ***write_BLock()***

     - Take user data, and the cluster number where it should write on

     - write what user enter into the virtual disk

       

   - ***read_BLock()***

     - Take the cluster number which user want to read/print.

       

3. #### Class FAT

   - ***Instructor()*** 

     - create array of 1024 byte

     - First 5 items is -1

     - The rest is zeros

       

   - ***Write_Fat_Table()***

     - Writes fat table into virtual disk

       

   - ***Get_available_cluster()***

     - Returns the index of first empty item of fat

       

   - ***Get_Next()***

     - Take the index that user want to display it's value and print it

       

   - ***Set_Next()***

     - Take user data and index to write on
     - place user data in fat table



4. #### Directory_Entry

   - ***Instructor()*** 

     - Take File name, File attribute, First cluster, File size, File if empty

       

   - ***get_dirEntry()***

     - Return Entry (Array) of 32 byte

     

   - ***print_dirFile()*** NOT REQUIRED

     - Write entry to txt file

       

5. #### Directory:

   - ***Instructor()*** 

     - Store all directory entries in on one directory array

       

   - ***print_Dir()**

     - print directory array

       

   - ***Write_Directory()***

     - 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
