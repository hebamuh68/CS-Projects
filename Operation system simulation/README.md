# OS simulation

It's a Python project to simulate the operating system.



## Classes & Functions

1. #### **Class CMD:** 

   - ***shell_commands:*** This use os library to access shell commands through the IDE

     

2. #### **Class VirtualDisk:**

   - ***Instructor**:* 

     - create txt of 1MB conatins 1024 clusters/Blocks of size 1024 byte 

     - first cluster full of "0" =========> Super_Block

     - The next 4 cluster full of "*" ====> Meta_Data

     - The rest of 1MB contain "#" ====> File_Data

       

   - ***write_BLock:***

     - Take user data, and the cluster number where it should write on

     - write what user enter into the virtual disk

       

   - ***read_BLock:***

     - Take the cluster number which user want to read/print.

       

3. #### Class FAT

   - ***Instructor**:* 

     - create array of 1024 byte

     - First 5 items is zeros

     - The rest is -1s

       

   - ***Write_Fat_Table:***

     - It writes fat table into virtual disk

       

   - ***Get_available_cluster:***

     - 

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
