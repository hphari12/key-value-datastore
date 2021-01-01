#import as library
import code 
#key and value with no expTime
code.create("A",{"AAA":1})
code.create("B",{"BBB":2})
#key,value and expireTime
code.create("C",{"CCC":3},10)
code.create("D",{"DDD":4},1)
#Read operation
code.read("A")
code.read("B")
#delete operation
code.delete("A")
#for multithreading
#t1=Thread(target=function,args=arguments)
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
#starting thread 1
t1.start()
t1.join()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
#starting thread 2
t2.start()
t2.join()
