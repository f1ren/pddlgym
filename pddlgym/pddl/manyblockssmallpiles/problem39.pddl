
(define (problem manyblockssmallpiles) (:domain blocks)
  (:objects
        b0 - block
	b1 - block
	b10 - block
	b11 - block
	b12 - block
	b13 - block
	b14 - block
	b15 - block
	b16 - block
	b17 - block
	b18 - block
	b19 - block
	b2 - block
	b20 - block
	b21 - block
	b22 - block
	b23 - block
	b24 - block
	b25 - block
	b26 - block
	b27 - block
	b28 - block
	b29 - block
	b3 - block
	b30 - block
	b31 - block
	b32 - block
	b33 - block
	b34 - block
	b35 - block
	b36 - block
	b4 - block
	b5 - block
	b6 - block
	b7 - block
	b8 - block
	b9 - block
  )
  (:init 
	(clear b0)
	(clear b10)
	(clear b13)
	(clear b14)
	(clear b17)
	(clear b20)
	(clear b23)
	(clear b24)
	(clear b25)
	(clear b27)
	(clear b29)
	(clear b30)
	(clear b32)
	(clear b33)
	(clear b34)
	(clear b35)
	(clear b3)
	(clear b4)
	(clear b6)
	(clear b9)
	(handempty )
	(on b0 b1)
	(on b10 b11)
	(on b11 b12)
	(on b14 b15)
	(on b15 b16)
	(on b17 b18)
	(on b18 b19)
	(on b1 b2)
	(on b20 b21)
	(on b21 b22)
	(on b25 b26)
	(on b27 b28)
	(on b30 b31)
	(on b35 b36)
	(on b4 b5)
	(on b6 b7)
	(on b7 b8)
	(ontable b12)
	(ontable b13)
	(ontable b16)
	(ontable b19)
	(ontable b22)
	(ontable b23)
	(ontable b24)
	(ontable b26)
	(ontable b28)
	(ontable b29)
	(ontable b2)
	(ontable b31)
	(ontable b32)
	(ontable b33)
	(ontable b34)
	(ontable b36)
	(ontable b3)
	(ontable b5)
	(ontable b8)
	(ontable b9)
  )
  (:goal (and
	(on b13 b21)
	(on b21 b30)
	(on b30 b31)
	(on b31 b3)
	(on b3 b10)
	(ontable b10)))
)