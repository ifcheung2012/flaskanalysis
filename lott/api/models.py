# coding: utf-8
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Text, text
from sqlalchemy.orm import relationship

from lott.ext import db
from lott.utils.algorithms import *


class Algorithm(db.Model):
    __tablename__ = 'algorithm'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(100))
    status = Column(Integer)
    rmv = Column(Integer)
    created = Column(DateTime)


class Doublechrom(db.Model):
    __tablename__ = 'doublechrom'

    id = Column(Integer, primary_key=True)
    lott_catid = Column(Integer)
    result = Column(String(50), nullable=False, server_default=text("''"))
    result_byorder = Column(String(50), nullable=False, server_default=text("''"))
    open_date = Column(String(20))
    issue = Column(String(20), server_default=text("''"))

    def get_all_douballs(self):
        douballs = Doublechrom.query.all()
        return douballs

    def get_douball_byissue(self, issue):
        douball = Doublechrom.query.filter(Doublechrom.issue == issue).one()
        return douball

    @staticmethod
    def get_top_list(topcounts):
        dboutput = Doublechrom.query.all()
        lottlist = [i.result[:17].split(' ') for i in dboutput]
        return alg_get_top_list(lottlist, topcounts=topcounts)

    @staticmethod
    def get_random_list(counts):
        dboutput = Doublechrom.query().all()

        lottlist = [set(i.result[:17].split(' ')) for i in dboutput]
        print(lottlist)
        other = alg_getrandom_one_from_combinations(lottlist, counts)
        print(other)
        random_list = set(lottlist) & set(other)
        return random_list
        # return lottlist


class Lottanalysi(db.Model):
    __tablename__ = 'lottanalysis'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    analysis = Column(Text, nullable=False)
    rmv = Column(Integer)


class Lottcat(db.Model):
    __tablename__ = 'lottcat'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    created = Column(DateTime)
    rmv = Column(Integer)


class Lotterydoublechrom(db.Model):
    __tablename__ = 'lotterydoublechrom'

    id = Column(Integer, primary_key=True)
    lottcat_id = Column(ForeignKey(u'lottcat.id'), nullable=False, index=True)
    issue = Column(String(20), nullable=False)
    opendate = Column(Date)
    redball = Column(String(20), nullable=False)
    redone = Column(String(2), nullable=False)
    redtwo = Column(String(2), nullable=False)
    redthree = Column(String(2), nullable=False)
    redfour = Column(String(2), nullable=False)
    redfive = Column(String(2), nullable=False)
    redsix = Column(String(2), nullable=False)
    blueball = Column(String(2), nullable=False)
    created = Column(DateTime)
    rmv = Column(Integer)

    lottcat = relationship(u'Lottcat')


class Lotterysuperlotto(db.Model):
    __tablename__ = 'lotterysuperlotto'

    id = Column(Integer, primary_key=True)
    lottcat_id = Column(ForeignKey(u'lottcat.id'), nullable=False, index=True)
    issue = Column(String(20), nullable=False)
    opendate = Column(Date)
    redball = Column(String(20), nullable=False)
    redone = Column(String(2), nullable=False)
    redtwo = Column(String(2), nullable=False)
    redthree = Column(String(2), nullable=False)
    redfour = Column(String(2), nullable=False)
    redfive = Column(String(2), nullable=False)
    blueball = Column(String(8), nullable=False)
    blueone = Column(String(2), nullable=False)
    bluetwo = Column(String(2), nullable=False)
    created = Column(DateTime)
    rmv = Column(Integer)

    lottcat = relationship(u'Lottcat')


class Lottforecast(db.Model):
    __tablename__ = 'lottforecast'

    id = Column(Integer, primary_key=True)
    lottcat_id = Column(ForeignKey(u'lottcat.id'), nullable=False, index=True)
    lottanalysis_id = Column(ForeignKey(u'lottanalysis.id'), nullable=False, index=True)
    issue = Column(Integer, nullable=False)
    forecastdata = Column(String(20))
    created = Column(DateTime)
    rmv = Column(Integer)

    lottanalysis = relationship(u'Lottanalysi')
    lottcat = relationship(u'Lottcat')


class Permit(db.Model):
    __tablename__ = 'permit'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(100))
    status = Column(Integer)
    rmv = Column(Integer)
    created = Column(DateTime)


class PermitAlgo(db.Model):
    __tablename__ = 'permit_algo'

    id = Column(Integer, primary_key=True)
    permit_id = Column(ForeignKey(u'permit.id'), nullable=False, index=True)
    algo_id = Column(ForeignKey(u'algorithm.id'), nullable=False, index=True)
    status = Column(Integer)
    rmv = Column(Integer)
    created = Column(DateTime)

    algo = relationship(u'Algorithm')
    permit = relationship(u'Permit')


class Role(db.Model):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    description = Column(String(100))
    status = Column(Integer)
    rmv = Column(Integer)
    created = Column(DateTime)


class RolePermit(db.Model):
    __tablename__ = 'role_permit'

    id = Column(Integer, primary_key=True)
    permit_id = Column(ForeignKey(u'permit.id'), nullable=False, index=True)
    role_id = Column(ForeignKey(u'role.id'), nullable=False, index=True)
    status = Column(Integer)
    rmv = Column(Integer)
    created = Column(DateTime)

    permit = relationship(u'Permit')
    role = relationship(u'Role')


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    passwd = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    sex = Column(Integer)
    birthday = Column(String(50))
    img = Column(String(255))
    info = Column(String(500))
    province = Column(String(50))
    city = Column(String(50))
    address = Column(String(50))
    ip = Column(String(15))
    last_ip = Column(String(15))
    status = Column(Integer)
    rmv = Column(Integer)
    created = Column(DateTime)


class UserRole(db.Model):
    __tablename__ = 'user_role'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey(u'user.id'), nullable=False, index=True)
    role_id = Column(ForeignKey(u'role.id'), nullable=False, index=True)
    status = Column(Integer)
    rmv = Column(Integer)
    created = Column(DateTime)

    role = relationship(u'Role')
    user = relationship(u'User')
