## What is this?

A project to indicate if a person or object is detected within a range of safety zones, by illuminating an RGB LED, sounding a tone, displaying a graphic and/or scrolling message.  Created for the [BBC micro:bit V2 computer](https://microbit.org) interfaced with an Osoyoo sensors & devices STEM kit and a third-party interface board.

LED colours indicate:

* Red = 'danger',
* Amber = 'unsafe',
* Green = 'safe'.

![Photo with Lego!](/img/microbit-proximity_photo.jpeg)

## Enhancements

I've always intended this for my work desk; the next steps will likely be the addition of the LCD display to refine the messaging.

## What is a BBC micro:bit?

An [embedded system](https://en.wikipedia.org/wiki/Embedded_system) computer, with dimensions half the size of a credit card.  Code must be written on a computer or a portable device before 'flashing' the program to the micro:bit via a either USB cable or Bluetooth.

## How was the program created?

It uses the Microsoft MakeCode IDE (blocks of code similar to Scratch.) In this case all the coding has used [the iPhone micro:bit app](https://apps.apple.com/gb/app/micro-bit/id1092687276).  However, [other platforms, apps and languages](https://microbit.org/code/) can be used.

Note: I have used only the block editor so be aware that the underlying 'written' code may not be ordered 'neatly'.  *(I originally thought the MicroPython code from the app would be saved here but only the javascript makes it to the repo; see the Main.ts file.)*

## The Osoyoo interface board and sensors

Various breakout boards are available, but I chose the [Osoyoo STEM Kit for micro:bit.](https://osoyoo.com/2019/06/13/osoyoo-steam-kit-for-microbit/)  The kit comprises the board, 20 sensors & devices, cables with connectors, an IR remote, an instruction CD, all packaged up in a sturdy box.

The third-party board does mot replicate the connector pinout order so I've not named it here.

## micro:bit pinout documentation

I made the rookie mistake of thinking all the micro:bit and thus the Osoyoo board pins would be addressable identically.  This is not the case.  Here is the official documentation:

[https://makecode.microbit.org/device/pins](https://makecode.microbit.org/device/pins)

## Meta

> Open this page at [https://bazbt3.github.io/microbit-proximity/](https://bazbt3.github.io/microbit-proximity/)

## Edit this project ![Build status badge](https://github.com/bazbt3/microbit-proximity/workflows/MakeCode/badge.svg)

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/bazbt3/microbit-proximity** and click import

## Blocks preview

This image shows the blocks code from the last commit in master.
This image may take a few minutes to refresh.

![A rendered view of the blocks](https://github.com/bazbt3/microbit-proximity/raw/master/.github/makecode/blocks.png)

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
