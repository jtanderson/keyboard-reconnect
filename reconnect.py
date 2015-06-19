#!/usr/bin/python

import usb1

print("Searching for device...")

ctx = usb1.USBContext()
devices = ctx.getDeviceList()

for device in devices:
  try:
    name = device.getProduct()
    print(name)
  except Exception as e:
    print(e)

  if name == "DasKeyboard":
    print("Found device...")
    try:
      targetHandle = device.open()
    except Exception as e:
      print("Could not open device")

    print("Attempting to reset...")
    try:
      # targetHandle.resetDevice()
      conf = targetHandle.getConfiguration()
      targetHandle.setConfiguration(conf)
    except Exception as e:
      print("Could not reset.")
    break
