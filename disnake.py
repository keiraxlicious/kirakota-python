from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
#models.py

engine = create_engine("sqlite://", echo=True, future=True)
Base = declarative_base()


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    # # # # # # # # # 

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Command(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    sub_commands = relationship("SubCommand", back_populates="command")

class SubCommand(Base):
    __tablename__ = "sub_commands"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    command_id = Column(Integer, ForeignKey("commands.id"))
    command = relationship("Command", back_populates="sub_commands")


    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    # # # # # # # # # Guilds

    # # # # # # # # # # # # Requires

    # # # # # # # # # # # # # # # Guild that holds Members, the roles they have, the permissions the roles have,

    # # # # # # # # # # # # # # # guild id, member id, channel id, category id,

    # # # # # # # # # # # # # # # each member is assigned to a guild id.

    # # # # # # # # # # # # # # # 

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Guild(Base):
    __tablename__ = "guilds"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_active = Column(Boolean)
    members = relationship("Member", back_populates="guild")
    roles = relationship("Role", back_populates="guild")
    channels = relationship("Channel", back_populates="guild")
    categories = relationship("Category", back_populates="guild")

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    guild_id = Column(Integer, ForeignKey("guilds.id"))
    guild = relationship("Guild", back_populates="members")
    activity_status = Column(String)

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    guild_id = Column(Integer, ForeignKey("guilds.id"))
    guild = relationship("Guild", back_populates="roles")

class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    guild_id = Column(Integer, ForeignKey("guilds.id"))
    guild = relationship("Guild", back_populates="channels")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    guild_id = Column(Integer, ForeignKey("guilds.id"))
    guild = relationship("Guild", back_populates="categories")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    # # # # # # # # # General Concept

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
"""
class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship(
    "Address", back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
"""
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

    # # # # # # # # # Level System

    # # # # # # # # # # # # Requires

    # # # # # # # # # # # # # # # XP

    # # # # # # # # # # # # # # # Levels

    # # # # # # # # # # # # # # # on level unlock perk

    # # # # # # # # # # # # # # # on level