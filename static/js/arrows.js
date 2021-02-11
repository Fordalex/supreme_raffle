
anime.set('.arrow-top', {
    rotateZ: 22,
});

anime.set('.arrow-mid', {
    rotateZ: '-200deg',
});

anime.set('.arrow-bottom', {
    rotateZ: '-102deg',
});



anime({
    targets: '.arrow-top',
    easing: 'easeInOutQuad',
    translateX: 70,
    translateY: 10,
    rotateZ: 32,
    loop: true,
    duration: 1000,
    direction: 'alternate',
  });

  anime({
    targets: '.arrow-mid',
    easing: 'easeInOutQuad',
    translateY: -30,
    translateX: 37,
    rotateZ: '-220deg',
    loop: true,
    duration: 930,
    direction: 'alternate',
  });

  anime({
    targets: '.arrow-bottom',
    easing: 'easeInOutQuad',
    translateY: 60,
    translateX: 60,
    rotateZ: '-132deg',
    loop: true,
    duration: 970,
    direction: 'alternate',
  });

console.log('working')