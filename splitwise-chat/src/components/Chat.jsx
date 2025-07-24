import React, { forwardRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Bot, User } from 'lucide-react';
import { useTheme } from '../theme';
import TypingIndicator from './TypingIndicator';

const Message = forwardRef(({ message, index }, ref) => {
  const { isDark } = useTheme();
  const isUser = message.sender === 'user';
  
  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 20, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ 
        duration: 0.3, 
        delay: index * 0.1,
        type: "spring",
        stiffness: 200,
        damping: 20
      }}
      className={`flex items-start space-x-3 ${isUser ? 'flex-row-reverse space-x-reverse' : ''}`}
    >
      {/* Avatar */}
      <motion.div
        whileHover={{ scale: 1.05 }}
        className={`flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center ${
          isUser 
            ? isDark ? 'bg-blue-600' : 'bg-blue-500'
            : isDark ? 'bg-gray-700' : 'bg-gray-200'
        }`}
      >
        {isUser ? (
          <User className="w-5 h-5 text-white" />
        ) : (
          <Bot className={`w-5 h-5 ${isDark ? 'text-gray-300' : 'text-gray-600'}`} />
        )}
      </motion.div>

      {/* Message Bubble */}
      <motion.div
        whileHover={{ scale: 1.02 }}
        className={`max-w-xs sm:max-w-md lg:max-w-lg xl:max-w-xl relative ${
          isUser ? 'ml-auto' : 'mr-auto'
        }`}
      >
        <div
          className={`px-4 py-3 rounded-2xl shadow-sm transition-all duration-200 ${
            isUser
              ? isDark 
                ? 'bg-blue-600 text-white' 
                : 'bg-blue-500 text-white'
              : isDark
                ? 'bg-gray-800 text-gray-100 border border-gray-700'
                : 'bg-white text-gray-900 border border-gray-200'
          } ${
            isUser ? 'rounded-br-md' : 'rounded-bl-md'
          }`}
        >
          <p className="text-sm leading-relaxed whitespace-pre-wrap">
            {message.text}
          </p>
        </div>
        
        {/* Timestamp */}
        <p className={`text-xs mt-1 ${
          isUser ? 'text-right' : 'text-left'
        } ${
          isDark ? 'text-gray-500' : 'text-gray-400'
        }`}>
          {message.timestamp && new Date(message.timestamp).toLocaleTimeString([], { 
            hour: '2-digit', 
            minute: '2-digit' 
          })}
        </p>
      </motion.div>
    </motion.div>
  );
});

export default function Chat({ messages, isTyping }) {
  return (
    <div className="space-y-6">
      <AnimatePresence mode="popLayout">
        {messages.map((message, index) => (
          <Message key={message.id} message={message} index={index} />
        ))}
        
        {isTyping && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="flex items-start space-x-3"
          >
            <TypingIndicator />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
