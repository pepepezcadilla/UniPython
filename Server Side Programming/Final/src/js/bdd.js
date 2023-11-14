var juegos = {}, i = 0, key = null, key2 = null

juegos = {
    nintendo: {
        IIIds: [
            { 
                ID: 'donkeyKong',
                nombre: 'Donkey Kong',
                src: './src/imagenes/videojuegos/nintendo/3ds/dk.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/y-eQ8jlxeW0?si=4UUOQNR12lyxExGA',
                stock: 10
            },
            { 
                ID: 'inazumaEleven',
                nombre: 'Inazuma Eleven',
                src: './src/imagenes/videojuegos/nintendo/3ds/inazuma.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/9YEQPU5RvfA?si=tGsnxUogXI9DlaEh',
                stock: 10
            },
            { 
                ID: 'kirby',
                nombre: 'Kirby',
                src: './src/imagenes/videojuegos/nintendo/3ds/Kirby.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/JiXCgnSlQOA?si=hp7j3Fxf9XKssPip',
                stock: 10
            },
            { 
                ID: 'marioMaker',
                nombre: 'Super Mario Maker',
                src: './src/imagenes/videojuegos/nintendo/3ds/maker.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/1U1YTJtMdRM?si=iEQd2eeqm-sUZ38o',
                stock: 10
            },
            { 
                ID: 'luigiMansion2',
                nombre: 'Luigis Mansion 2',
                src: './src/imagenes/videojuegos/nintendo/3ds/mansion2.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/QiqNL4QlrpM?si=k_GB9cBoeDyO1ZLX',
                stock: 10
            },
            { 
                ID: 'animalCrossing',
                nombre: 'Animal Crossing New Leaf',
                src: './src/imagenes/videojuegos/nintendo/3ds/newleaf.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/z09iRo44Mcs?si=We8xwD1UY-EIJRiC',
                stock: 10
            },
            { 
                ID: 'ninjago',
                nombre: 'Lego Ninjago',
                src: './src/imagenes/videojuegos/nintendo/3ds/ninjago.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/Ci941DI07us?si=WhwYj7zV3eI3NYy8',
                stock: 10
            },
            { 
                ID: 'ocarina',
                nombre: 'The legend of Zelda: Ocarina of time 3D',
                src: './src/imagenes/videojuegos/nintendo/3ds/ocarina.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/r2blfz172Iw?si=_4SKods2vU_CNsot',
                stock: 10
            },
            { 
                ID: 'zafiro',
                nombre: 'Pokemon Zafiro Alfa',
                src: './src/imagenes/videojuegos/nintendo/3ds/zafiro.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/pRhKHviy0Qs?si=GCNV47QO-gpns3V-',
                stock: 10
            }
        ],
        switch: [
            { 
                ID: 'animal',
                nombre: 'Animal Crossing New horizons',
                src: './src/imagenes/videojuegos/nintendo/switch/animal.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/5YPxiTLMcdg?si=P_LKRwKmsDi_ZRej',
                stock: 10
            },
            { 
                ID: 'breath',
                nombre: 'The legend of Zelda: Breath of the Wild',
                src: './src/imagenes/videojuegos/nintendo/switch/breath.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/ofH5ptn5w-A?si=I5wZjeIvHu-GaYgJ',
                stock: 10
            },
            { 
                ID: 'kart',
                nombre: 'Mario kart 8 deluxe',
                src: './src/imagenes/videojuegos/nintendo/switch/kart.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/N_Hw_M5ENCQ?si=_-hgJriecz-Hdah6',
                stock: 10
            },
            { 
                ID: 'kirbiS',
                nombre: 'Kirby y la tierra olvidada',
                src: './src/imagenes/videojuegos/nintendo/switch/kirbi.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/H3LAkr0ANgw?si=UQ-4Sk1ENz8ctHfb',
                stock: 10
            },
            { 
                ID: 'luigiMansion3',
                nombre: 'Luigis mansion 3',
                src: './src/imagenes/videojuegos/nintendo/switch/mansion3.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/RSGgCfbYrg0?si=6xswIwx3VjofdI1M',
                stock: 10
            },
            { 
                ID: 'mario3d',
                nombre: 'Super Mario 3d World',
                src: './src/imagenes/videojuegos/nintendo/switch/mario3d.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/OPAQA_P_RQY?si=Npwlvs0UAh-plsSb',
                stock: 10
            },
            { 
                ID: 'odyssey',
                nombre: 'Super Mario Odyssey',
                src: './src/imagenes/videojuegos/nintendo/switch/odyssey.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/EF5YynyWvQo?si=HT4kceSlBkIUyt4x',
                stock: 10
            },
            { 
                ID: 'pkm',
                nombre: 'Pokemon Purpura',
                src: './src/imagenes/videojuegos/nintendo/switch/pkm.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/wSjreMPrHeg?si=tbXo7b5vIHfO-SW-',
                stock: 10
            },
            { 
                ID: 'tears',
                nombre: 'The legend of Zelda: Tears of the Kingdom',
                src: './src/imagenes/videojuegos/nintendo/switch/tears.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/gp9aY09li1s?si=6maOAL22zM1YQmry',
                stock: 10
            }
        ]
    },
    pc: {
        // TODO
    },
    playStation: {
        psIV: [
            { 
                ID: 'detroit',
                nombre: 'Dertoit: Become human',
                src: './src/imagenes/videojuegos/playstation/ps4/detroit.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/euULGCe8Y50?si=dXOPQheXGS0qfCYC',
                stock: 10
            },
            { 
                ID: 'fallenOrder',
                nombre: 'Stars Wars: Jedi fallen Order',
                src: './src/imagenes/videojuegos/playstation/ps4/fallenorder.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/x5SPx89Bg1Q?si=Y0dueQxrmfCZnyQh',
                stock: 10
            },
            { 
                ID: 'god',
                nombre: 'God of War',
                src: './src/imagenes/videojuegos/playstation/ps4/god.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/dK42JGgkoF8?si=umxHeNf7xt5GPaT6',
                stock: 10
            },
            { 
                ID: 'lastOfUs',
                nombre: 'The last of us',
                src: './src/imagenes/videojuegos/playstation/ps4/lastofus.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/AaOWRvmtEFQ?si=YunGcapTTZj-Ydly',
                stock: 10
            },
            { 
                ID: 'rainbow',
                nombre: 'Rainbow Six Siege',
                src: './src/imagenes/videojuegos/playstation/ps4/rainbow.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/Vsc4_c3HxTQ?si=3SYGxIegSzB9TU_4',
                stock: 10
            },
            { 
                ID: 'rd2',
                nombre: 'Red dead Redemption 2',
                src: './src/imagenes/videojuegos/playstation/ps4/rd2.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/JXZKLfLZkv8?si=gJHP2CF-QunvEBjo',
                stock: 10
            },
            { 
                ID: 'spidey',
                nombre: 'Spider-man',
                src: './src/imagenes/videojuegos/playstation/ps4/spidey.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/UpCrjE2hW-k?si=HOcZbx0I_LpH7XO8',
                stock: 10
            },
            { 
                ID: 'tsushima',
                nombre: 'Gost of Tsushima',
                src: './src/imagenes/videojuegos/playstation/ps4/tsushima.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/jT9edKarhc8?si=ZCWfeV7UD1hTJL5N',
                stock: 10
            },
            { 
                ID: 'uncharted',
                nombre: 'Uncharted the collection',
                src: './src/imagenes/videojuegos/playstation/ps4/uncharted.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/LvC_K087qvk?si=xQg2pV-u8biegZGn',
                stock: 10
            }
        ],
        psV: [
            { 
                ID: 'godV',
                nombre: 'God of war: Ragnarok',
                src: './src/imagenes/videojuegos/playstation/ps5/god.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=jb0LtQBNqhY&ab_channel=PlayStationEspa%C3%B1a',
                stock: 10
            },
            { 
                ID: 'gt7',
                nombre: 'Gran Turismo 7',
                src: './src/imagenes/videojuegos/playstation/ps5/gt7.png',
                precio: 30,
                videoURL: '',
                stock: 10
            },
            { 
                ID: 'last1',
                nombre: 'The last of Us:  Parte1',
                src: './src/imagenes/videojuegos/playstation/ps5/last1.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=1tBUsXIkG1A&ab_channel=PlayStation',
                stock: 10
            },
            { 
                ID: 'miles',
                nombre: 'Spider-man: Miles Morales',
                src: './src/imagenes/videojuegos/playstation/ps5/miles.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=Q3kfF3XNzw8&ab_channel=PlayStationEspa%C3%B1a',
                stock: 10
            },
            { 
                ID: 'ratchet',
                nombre: 'Rachet & Clank',
                src: './src/imagenes/videojuegos/playstation/ps5/ratchet.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=IkPWYH403tU&ab_channel=PlayStationEspa%C3%B1a',
                stock: 10
            },
            { 
                ID: 'survivor',
                nombre: 'Star Wars: Jedi survivor',
                src: './src/imagenes/videojuegos/playstation/ps5/survivor.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=w9Z2a5Faj3c&ab_channel=PlayStation',
                stock: 10
            },
            { 
                ID: 'witcher',
                nombre: 'The Witcher 3',
                src: './src/imagenes/videojuegos/playstation/ps5/witcher.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=6_WDVEw9YUo&ab_channel=PlayStation',
                stock: 10
            },
            { 
                ID: 'yakuza',
                nombre: 'Yakuza: Like a Dragon',
                src: './src/imagenes/videojuegos/playstation/ps5/yakuza.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=4w092H6K0XM&ab_channel=PlayStation',
                stock: 10
            },
            { 
                ID: 'gta',
                nombre: 'Grand Theft Auto V',
                src: './src/imagenes/videojuegos/playstation/ps5/gta.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=dIofO2jAF8k&ab_channel=PlayStationEspa%C3%B1a',
                stock: 10
            }
        ]
    },
    xbox: {
        one: [
            { 
                ID: 'dead',
                nombre: 'Dead Space',
                src: './src/imagenes/videojuegos/xbox/dead.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=_iXrSpyPces&ab_channel=Xbox',
                stock: 10
            },
            { 
                ID: 'dead2',
                nombre: 'Dead island 2',
                src: './src/imagenes/videojuegos/xbox/dead2.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=yqvnKCqgGH0&ab_channel=Xbox',
                stock: 10
            },
            { 
                ID: 'farcry6',
                nombre: 'Far Cry 6',
                src: './src/imagenes/videojuegos/xbox/farcry6.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=tdOQbgL9f1E&ab_channel=Xbox',
                stock: 10
            },
            {
                ID: 'forza',
                nombre: 'Forza MotorSport',
                src: './src/imagenes/videojuegos/xbox/forza.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/yJumrR_bbg0?si=zkvZ91Q8PHGZ26Pg',
                stock: 10
            },
            { 
                ID: 'halo',
                nombre: 'Halo Infinite',
                src: './src/imagenes/videojuegos/xbox/halo.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=rFh2i4AlPD4&ab_channel=HALO',
                stock: 10
            },
            { 
                ID: 'hogwarts',
                nombre: 'Hogwarts Legacy',
                src: './src/imagenes/videojuegos/xbox/hogwarts.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=BtyBjOW8sGY&ab_channel=HogwartsLegacy',
                stock: 10
            },
            { 
                ID: 'kakarot',
                nombre: 'Dragon ball Z: Kakarot',
                src: './src/imagenes/videojuegos/xbox/kakarot.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=60Ogtp_2mV8&ab_channel=Xbox',
                stock: 10
            },
            { 
                ID: 'midnight',
                nombre: 'Midnight Suns',
                src: './src/imagenes/videojuegos/xbox/midnight.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/watch?v=Ripgh8W2PMg&ab_channel=MarvelEntertainment',
                stock: 10
            },
            { 
                ID: 'starfield',
                nombre: 'Starfield',
                src: './src/imagenes/videojuegos/xbox/starfield.png',
                precio: 30,
                videoURL: 'https://www.youtube.com/embed/pYqyVpCV-3c?si=XuPsvF7wfhghgwKr',
                stock: 10
            }
        ]
    },
}

function getJuego(plataforma, consola, id){
    for (let key in juegos) {
        console.log('%cbdd.js line:387 key', 'color: #007acc;', key);
        if (key === plataforma) {
            for (let key2 in juegos[plataforma]) {
                if (key2 === consola) {
                    for (i = 0; i < juegos[plataforma][consola].length; i++) {
                        if (juegos[plataforma][consola][i].ID === id) {
                            return juegos[plataforma][consola][i];
                        }
                    }
                    return 'Juego no encontrado';
                }
            }
            return 'Consola no encontrada'
        }
    }
    return 'Plataforma no encontrada'
}

function getAll(){
    return juegos;
}

function reduceJuego(plataforma, consola, id) {
    if (juegos[plataforma] === plataforma) {
        if (juegos[consola] === consola) {
            for (i = 0; i < juegos[consola].length; i++) {
                if (juegos[consola][i].id === id) {
                    if (juegos[consola][i].stock < 0){
                        juegos[consola][i].stock --;
                        return juegos[consola][i];
                    } else {
                        return 'No hay stock';
                    }
                }
            }
            return 'Juego no encontrado';
        } else {
            return 'Consola no encontrada'
        }
    } else {
        return 'Plataforma no encontrada'
    }
}

export {getJuego};