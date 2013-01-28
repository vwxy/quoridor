import web, daisy, lilac

urls = ('/', 'index')

class index:
    def GET(self):
        q = web.ctx.query
        if not q:
            return 'nada'
        else:
            p = q.split(':')
            if len(p)==1 or not p[1]:
                history = []
            else:
                history = p[1].split(',')
            if p[0] == '?search':
                pawn_moves = [str(x[0]*9+x[1]) for x in list(daisy.pawn_moves(history))]
                return ','.join(pawn_moves+list(daisy.wall_moves(history)))
            elif p[0] == '?daisy':
                player = daisy
            elif p[0] == '?lilac':
                player = lilac
            else:
                return 'unknown player'
            return player.next_move(history)

if __name__ == '__main__':     
    app = web.application(urls, globals())
    app.run()
