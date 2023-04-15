from django.contrib import admin

from .models import Conversation, Message, Setting
from .models import Deposit, Balance, MessageCost


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'topic', 'created_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_conversation_topic', 'message', 'total_token', 'is_bot', 'created_at')

    def get_conversation_topic(self, obj):
        return obj.conversation.topic

    get_conversation_topic.short_description = 'Conversation Topic'

@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'currency', 'exchange', 'source')

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'usd_amount')

@admin.register(MessageCost)
class MessageCostAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_message_id', 'get_message_token', 'usd_amount')

    def get_message_token(self, obj):
        return obj.message.total_token

    get_message_token.short_description = 'Total Token'

    def get_message_id(self, obj):
        return obj.message.id

    get_message_id.short_description = 'Msg ID'
