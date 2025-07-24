import { motion } from 'framer-motion';
import { Users, Plus, List, DollarSign } from 'lucide-react';
import { useTheme } from '../theme';

const quickActions = [
  {
    id: 'list-groups',
    label: 'List Groups',
    icon: Users,
    description: 'View all your groups'
  },
  {
    id: 'add-expense',
    label: 'Add Expense',
    icon: Plus,
    description: 'Create a new expense'
  },
  {
    id: 'recent-expenses',
    label: 'Recent Expenses',
    icon: List,
    description: 'View recent transactions'
  },
  {
    id: 'balances',
    label: 'Check Balances',
    icon: DollarSign,
    description: 'See who owes what'
  }
];

export default function QuickActions({ onAction }) {
  const { isDark } = useTheme();

  return (
    <div className="space-y-4">
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center"
      >
        <h2 className={`text-lg font-semibold mb-2 ${
          isDark ? 'text-white' : 'text-gray-900'
        }`}>
          Quick Actions
        </h2>
        <p className={`text-sm ${
          isDark ? 'text-gray-400' : 'text-gray-600'
        }`}>
          Get started with these common tasks
        </p>
      </motion.div>

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        {quickActions.map((action, index) => {
          const Icon = action.icon;
          return (
            <motion.button
              key={action.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              whileHover={{ scale: 1.05, y: -2 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => onAction(action.id)}
              className={`p-4 rounded-xl border transition-all duration-200 text-center group ${
                isDark
                  ? 'bg-gray-800 border-gray-700 hover:border-blue-500 hover:bg-gray-750'
                  : 'bg-white border-gray-200 hover:border-blue-400 hover:bg-blue-50'
              } shadow-sm hover:shadow-md`}
            >
              <div className={`w-8 h-8 mx-auto mb-2 rounded-lg flex items-center justify-center transition-colors duration-200 ${
                isDark
                  ? 'bg-gray-700 group-hover:bg-blue-600'
                  : 'bg-gray-100 group-hover:bg-blue-500'
              }`}>
                <Icon className={`w-4 h-4 transition-colors duration-200 ${
                  isDark
                    ? 'text-gray-300 group-hover:text-white'
                    : 'text-gray-600 group-hover:text-white'
                }`} />
              </div>
              <h3 className={`text-sm font-medium mb-1 ${
                isDark ? 'text-white' : 'text-gray-900'
              }`}>
                {action.label}
              </h3>
              <p className={`text-xs ${
                isDark ? 'text-gray-400' : 'text-gray-500'
              }`}>
                {action.description}
              </p>
            </motion.button>
          );
        })}
      </div>
    </div>
  );
}
