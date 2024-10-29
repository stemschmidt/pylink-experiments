Pre-Requisites on your host:
- git installed
- vscode installed, with plugins "Remote Containers", "Cortex-Debug"
- docker installed
- Segger JLinkServer
- python with additional modules matplotlib, pylink-square

How to use:
1. "git clone https://github.com/stemschmidt/vsc-nrf-sdk.git"
2. "cd vsc-nrf-sdk"
3. "code ." or open vsc-nrf-sdk in VSCode
4. in VSCode, select "reopen folder in container"
5. after docker image is downloaded and started, go to "TERMINAL" tab:
6. "west init -l application"
7. "west update"
8. "source zephyr/zephyr-env.sh"
9. "cd application"
10. "west build -b nrf9160dk_nrf9160_ns" and wait for the build to finish...

11. on the host, launch the JLinkGDBServer (e.g "JLinkGDBServerCLExe -if swd -device nRF9160_xxAA -vd")
12. on the host, launch the JLinkRTTViewer to see debug log (e.g "JLinkRTTViewer", select "Connection to J-Link" -> "Existing session")

13. Select "Run and Debug" icon in activity bar in VSCode --> Download binary and start debugging by launching "JLink" 


On your host, run "counter_viewer.py <device> <address in hex> <interval in ms>" which will use the JLink (using your configured device) to read the content of the counter variable at <address> every <interval> milliseconds and plots it.

You may stop the firmware in the debugger and notice, that the content of the variable does no longer increase. You can step over the '++counter' line and notice the single increment in the plot.

--> The debugger access is independent from the background memory access using two different paths to monitor the device.