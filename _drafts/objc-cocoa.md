---
layout: post
title: Objective-C, CocoaTouch and iOS development: A critic.
---



# Intro

http://learningiphoneprogramming.com/


This won't be an in-depth criticism of the development platform. There
won't be any praising, even if I think many things are really well
thought. Take that as an attempt of constructive criticism to take
this development platform to the next level.


I will cover a series of gripes I encountered while developping
applications with the classic Apple toolchain:

- Objective-C
- Foundation & CocoaTouch frameworks
- XCode 3


No language, framework or tool is perfect. I will continue to use this
platform. 



# Objective-C

Objective-C wants to be to Smalltalk what C++ is to Simula. It is a
superset of the C programming language, with a smalltalk-like
object model on top of it. This means much more reflexivity,
dynamism. I'm all for it.



## Memory management

Objective-C for iOS does not give you garbage collection. However, it
gives you reference counting, which is supposed to be a win compared
to the plain old malloc/free memory management scheme. 

My previous experience with reference
counting is through high level programming languages such as Python
and Ruby, or through the boost::shared_ptr in C++. I'm not going to
discuss the technical advantages 



In the end, Objective-C asks you to balance every alloc/copy/retain
with a release. 

From a user experience point of view, I have a hard time seeing the
advantage over plain old malloc/free strategy.


Autorelease is a nice gadget to defer the release
until we hit the local autorelease pool drain. 


## Messages & method names





# CocoaTouch, UIKit




# Documentation

Developing for iOS, you can't consider Objective-C without the Foundation
and CocoaTouch frameworks. It's the standard library. Any useful
application will likely be an assemblage of library calls. 


I've already outlined how the lack of scoped references made me add a
lot of cruft to my code, but it wouldn't be as painful if the framework
documentation was a little clearer concerning the ownership of
objects.


    NSMutableArray *indices = [[NSMutableArray alloc] init]; 
    [indices autorelease]; 
     
    for(int i=0; i < cities.count; i++ ) {
        [indices addObject:[NSIndexPath indexPathForRow:i inSection:0]];
    } 
     
    NSArray *lastIndex = [NSArray arrayWithObject:[NSIndexPath indexPathForRow:cities.count inSection:0]];
     
    for(int i=0; i < cities.count; i++ ) {
        UITableViewCell *cell = [tableView
        cellForRowAtIndexPath:[indices objectAtIndex:i]]; [cell setSelectionStyle:UITableViewCellSelectionStyleNone];
    } 


So, yeah, we're creating an NSMutableArray through alloc/init, so by
convention it is our responsability to release it. We choose here to
delay the release with autorelease.

Filling up the array with a bunch of NSIndexPath. We use the
convenience method indexPathForRow:inSection:, so this object is not
our responsability. However, adding 
