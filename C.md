## IDE选择： code:blocks

[参考资料1](https://linux.cn/article-5078-1.html) [参考资料2](http://www.cnblogs.com/Nimeux/archive/2010/07/07/1772788.html)


## c语言下多线程
[thread_reat参考资料](https://baike.baidu.com/item/pthread_create)

``` c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
 
#define    NUM_THREADS     8
 
void *PrintHello(void *args)
{
    int thread_arg;
    sleep(1);
    thread_arg = (int)(*((int*)args));
    printf("Hello from thread %d\n", thread_arg);
    return NULL;
}
 
int main(void)
{
    int rc,t;
    pthread_t thread[NUM_THREADS];
 
    for( t = 0; t < NUM_THREADS; t++)
    {
        printf("Creating thread %d\n", t);
        rc = pthread_create(&thread[t], NULL, PrintHello, &t);
        if (rc)
        {
            printf("ERROR; return code is %d\n", rc);
            return EXIT_FAILURE;
        }
    }
    sleep(5);
    for( t = 0; t < NUM_THREADS; t++)
        pthread_join(thread[t], NULL);
    return EXIT_SUCCESS;
}
```

编译，执行
```
g++ -o temp temp.c -lpthread
./temp

```
