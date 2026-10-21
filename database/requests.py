from database.models import Application
from database.database import session_maker


async def add_application(user_id, username, service, name, phone):
    async with session_maker() as session:
        new_app = Application(user_id=user_id,
                              username=username,
                              service=service,
                              name=name,
                              phone=phone)
        session.add(new_app)
        await session.commit()
