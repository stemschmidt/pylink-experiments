#include <zephyr/kernel.h>
#include <zephyr/logging/log.h>

LOG_MODULE_REGISTER(main);

static volatile int counter = 0;

int main(void) {
    while (1) {
        k_msleep(50);
        if(++counter > 50) {
          counter = 0;
          LOG_INF(".");
        }
    }

    return 0;
}
