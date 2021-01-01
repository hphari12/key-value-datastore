#import as library
import code1 
#key and value with no expTime
code1.create("A",{"AAA":1})
code1.create("B",{"BBB":2})
#key,value and expireTime
code1.create("C",{"CCC":3},10)
code1.create("D",{"DDD":4},1)
#Read operation
code1.read("A")
code1.read("B")
#delete operation
code1.delete("A")
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
