block = (22,0)
empty = (0,0)

class TempHouse: #inheritance
    blueprint = [
        [
            [block, block, block, block, block],
            [block, block, block, block, block],
            [block, block, block, block, block],
            [block, block, block, block, block],
            [block, block, block, block, block]
        ],
        [
            [block, block, block, block, block],
            [block, empty, empty, empty, block],
            [block, empty, empty, empty, block],
            [block, empty, empty, empty, block],
            [block, block, block, block, block]
        ],
        [
            [block, block, block, block, block],
            [block, empty, empty, empty, block],
            [block, empty, empty, empty, block],
            [block, empty, empty, empty, block],
            [block, block, block, block, block]
        ],
        [
            [block, block, block, block, block],
            [block, empty, empty, empty, block],
            [block, empty, empty, empty, block],
            [block, empty, empty, empty, block],
            [block, block, block, block, block]
        ],
        [
            [block, block, block, block, block],
            [block, block, block, block, block],
            [block, block, block, block, block],
            [block, block, block, block, block],
            [block, block, block, block, block]
        ]
    ]
    

    def get_blueprint(self):
        return self.blueprint
