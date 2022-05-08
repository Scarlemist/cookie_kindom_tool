from sqlalchemy import Column, Index, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy import VARCHAR
from sqlalchemy import Integer, Float, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cookie(Base):
	__tablename__ = 'cookies'
	__table_args__ = (
		{'extend_existing': True}
	)

	id = Column(Integer, primary_key=True, autoincrement=True)
	cookie_name = Column(VARCHAR(length=32), nullable=False)
	cool_time = Column(Integer, nullable=False)


class CookieTopping(Base):
	__tablename__ = 'cookie_toppings'
	__table_args__ = (
		{'extend_existing': True}
	)

	id = Column(Integer, primary_key=True, autoincrement=True)
	cookie_id = Column(Integer, nullable=False)
	part_num = Column(Integer, nullable=False)
	part_pos = Column(Integer, nullable=False)
	is_lock = Column(BOOLEAN, nullable=False)
	desc = Column(VARCHAR(length=64))
	top_id = Column(Integer)


class Topping(Base):
	__tablename__ = 'toppings'
	__table_args__ = (
		{'extend_existing': True}
		)

	id = Column(Integer, primary_key=True, autoincrement=True)
	type = Column(Integer, nullable=False)
	ATK = Column(Float, nullable=False, default=0)
	DEF = Column(Float, nullable=False, default=0)
	HP = Column(Float, nullable=False, default=0)
	SPD = Column(Float, nullable=False, default=0)
	CRIT = Column(Float, nullable=False, default=0)
	COOL = Column(Float, nullable=False, default=0)
	D_RESIST = Column(Float, nullable=False, default=0)
	C_RESIST = Column(Float, nullable=False, default=0)
	BUFF = Column(Float, nullable=False, default=0)
	DEBUFF = Column(Float, nullable=False, default=0)


class Record(Base):
	__tablename__ = 'records'
	__table_args__ = (
		PrimaryKeyConstraint('top_id', 'modify_time', name='record_key'),
		{'extend_existing': True}
		)

	top_id = Column(Integer, nullable=False)
	raw_cookie_id = Column(Integer, nullable=False)
	raw_desc = Column(VARCHAR(length=64))
	cur_cookie_id = Column(Integer, nullable=False)
	cur_desc = Column(VARCHAR(length=64))
	modify_time = Column(Integer, nullable=False)


class Color(Base):
	__tablename__ = 'color'
	__table_args__ = (
		PrimaryKeyConstraint('top_type', 'color', name='color_key'),
		{'extend_existing': True}
		)

	top_type = Column(Integer, nullable=False)
	color = Column(VARCHAR(length=6), nullable=False)
