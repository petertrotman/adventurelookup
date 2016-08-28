import React from 'react';

import './About.scss';

const About = () => (
  <div className="about">
    <h2>About</h2>
    <p>
      Wouldn't it be great to think "I want to run an adventure with a
      Beholder as the villain!" and be able to find a list of every published
      adventure featuring beholders? Then be able to pick the one you want
      based on your own criteria? Like. . .what level your party is, or whether
      the adventure is in a dungeon or on another plane?
    </p>
    <p align="center">
      <iframe
        width="640"
        height="360"
        src="https://www.youtube.com/embed/PIyLvicSu78"
        frameBorder="0"
      />
    </p>
    <p>
      Throughout the 40+ year history of the game, companies like TSR, Wizards
      of the Coast, the Judges' Guild, Goodman Games, and Paizo published
      thousands if not tens of thousands of adventures. Adventures of every
      kind and size, adventures on other planes, against every monster
      imaginable. Odds are, whatever adventure you're thinking of, whatever
      kind of quest you want to send your players on, someone has already done
      it.
    </p>
    <p>
      I believe that IF you could easily find that adventure, it would be
      easier to adapt it to your own campaign than create the entire thing from
      scratch.
    </p>
    <p>
      Therefore I propose a searchable tool, AdventureLookup.com, that will
      allow Dungeon Masters to find the adventure they're looking for.
    </p>
    <p>
      Each record is just a <strong>description</strong> of a published
      adventure. The content would come from us, the users. I have The Temple
      of Elemental Evil sitting right here, I can spend 10 minutes and fill in
      all the fields for it. Then anyone looking for an epic Greyhawk adventure
      that starts at 1st level and features Elementals would see The Temple of
      Elemental Evil in the search results.
    </p>
    <p>
      The site will not <strong>sell</strong> adventures, it just lets you know
      the adventure you're looking for is out there. It may include links to
      online stores where you can buy the official PDF or print product if
      these exist.
    </p>
    <p>
      Unfortunately, I am not a database programmer or a web developer. But
      it's my hope that by croudsourcing the solution, we can first create the
      tool, then populate it with content. It may take years to fill with
      adventures, it may never happen at all. But even if it happens very
      slowly, it will be a huge boon to DMs of all experience levels.
    </p>
    <p>
      -Matthew Colville
    </p>
  </div>
);

export default About;
