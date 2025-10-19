// Home split text
const { animate, splitText, stagger } = anime;
 
const { chars:chars1 } = splitText('.home-profession-1', {chars: true});
const { chars: chars2 } = splitText('.home-profession-2', { chars: true });

animate(chars1, {
  y: [
    { to: ['100%', '0%'] },
    { to: '-100%', delay: 4000, ease: 'in(3)' }
  ],
  duration: 900,
  ease: 'out(3)',
  delay: stagger(80),
  loop: true,
});

animate(chars2, {
  y: [
    { to: ['100%', '0%'] },
    { to: '-100%', delay: 4000, ease: 'in(3)' }
  ],
  duration: 900,
  ease: 'out(3)',
  delay: stagger(80),
  loop: true,
});


//  const { animate, splitText, stagger } = anime;

// const { chars:chars1 } = splitText('.home-profession-1', {chars: true});
// const { chars:chars2 } = splitText('.home-profession-2', {chars: true});

// animate(chars1, {
//   y: [
//     { to: ['100%', '0%'] },
//     { to: '-100%', delay: 4000, ease: 'in(3)' }
//   ],
//   duration: 900,
//   ease: 'out(3)',
//   delay: stagger(50),
//   loop: true,
// });
// animate(chars2, {
//   y: [
//     { to: ['100%', '0%'] },
//     { to: '-100%', delay: 4000, ease: 'in(3)' }
//   ],
//   duration: 900,
//   ease: 'out(3)',
//   delay: stagger(50),
//   loop: true,
// });


