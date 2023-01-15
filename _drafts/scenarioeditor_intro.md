---
layout: post
title:  "New B&S mod: Scenario Editor"
categories: jekyll update
hidden: true
hasArticle: false
---

I have been working on a new sandbox mod for Blade & Sorcery. I had the idea even before Dungeon Configurator for a mission editor that
would let you set up events in the world using some kind of a description language.
It originally started out as a scenario editor for my planned Undying scenarios but it grew into something more general.
The idea comes from the behavior trees that the game uses for AI as well as the behavior trees in Unreal Engine.
You use nodes in a tree structure to describe connections between game objects in the world to produce what's essentially a scene.
You can have multiple scenes and these can be triggered based on signals themselves.
You have some basic building blocks such as Locations which are 3d positions with a rotation, Triggers and Signals & Conditions and you use a combination
of these to build more complex systems.
It's basically a mini-programming language in the game.  
I have released an Alpha version which you can find under the Mods section.
It's still in it's infancy but you can already do a lot with it.
For a full set of features see: